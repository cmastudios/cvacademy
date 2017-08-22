import base64
import enum
import random
import string
import tempfile
import os
import subprocess


class ProgramLanguage(enum.Enum):
    PYTHON3 = 1
    CPLUSPLUS = 2


class ProgramResult(object):
    def __init__(self, output):
        self.output = output
        self.images = ''
        for file in os.listdir('.'):
            if file.endswith('_imshow.png'):
                with open(file, "rb") as image:
                    self.images += "<figure><figcaption>" + file.rstrip(
                        "_imshow.png") + "</figcaption><img src=\"data:image/png;base64," + base64.b64encode(
                        image.read()) + "\"></figure><br>"
                os.unlink(file)


class CompilationError(Exception):
    pass


def compile_cpp():
    with open('CMakeLists.txt', 'w') as f:
        f.write("project(cvacademy-{})\n".format(
            ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))))
        f.write("cmake_minimum_required(VERSION 2.8)\n")

        f.write("set(CMAKE_CXX_FLAGS \"${CMAKE_CXX_FLAGS} -std=c++11 -g -Wall\")\n")

        f.write("find_package(OpenCV)\n")

        f.write("add_executable(program program.cpp)\n")
        f.write("target_include_directories(program PUBLIC ${CMAKE_CURRENT_SOURCE_DIR} ${OpenCV2_INCLUDE_DIRS})\n")
        f.write("target_link_libraries(program LINK_PUBLIC ${OpenCV_LIBS})\n")
    cmake_out = subprocess.run('cmake .', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = cmake_out.stdout.decode('utf-8')
    if cmake_out.returncode != 0:
        raise CompilationError(output)
    make_out = subprocess.run('make', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = make_out.stdout.decode('utf-8')
    if make_out.returncode != 0:
        raise CompilationError(output)


def execute_cpp():
    proc = subprocess.run('ulimit -t 60; nice -n 15 ./program', shell=True, stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT)
    return "{}Process exited with return code {}.".format(proc.stdout.decode('utf-8'), proc.returncode)


def execute_py():
    proc = subprocess.run('ulimit -t 60; nice -n 15 python3 program.py', shell=True, stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT)
    return "{}Process exited with return code {}.".format(proc.stdout.decode('utf-8'), proc.returncode)


def compile_execute(code: str, language: ProgramLanguage) -> ProgramResult:
    pwd = os.open('.', os.O_RDONLY)
    with tempfile.TemporaryDirectory(prefix='cvacademy') as tempdir:
        os.chdir(tempdir)

        fn = 'program.py'
        if language == ProgramLanguage.CPLUSPLUS:
            fn = 'program.cpp'

        with open(fn, 'w') as f:
            f.write(code)

        try:
            if language == ProgramLanguage.CPLUSPLUS:
                compile_cpp()
                output = ProgramResult(output=execute_cpp())
            elif language == ProgramLanguage.PYTHON3:
                output = ProgramResult(output=execute_py())
            else:
                output = ProgramResult(output='Unsupported programming language')
        except CompilationError as e:
            output = ProgramResult(output=str(e))

    os.fchdir(pwd)
    os.close(pwd)
    return output
