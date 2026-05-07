def exception_hierarchy():
    'https://docs.python.org/3/library/exceptions.html#exception-hierarchy'
    try:
        # 테스트를 위해 아래 에러 중 하나를 발생시켜 보세요.
        raise FloatingPointError("FloatingPointError")
        """
            raise ArithmeticError("ArithmeticError")
            raise FloatingPointError("FloatingPointError")
            raise OverflowError("OverflowError")
            raise ZeroDivisionError("ZeroDivisionError")
            raise AssertionError("AssertionError")
            raise AttributeError("AttributeError")
            raise BufferError("BufferError")
            raise EOFError("EOFError")
            raise ImportError("ImportError")
            raise LookupError("LookupError")
            raise MemoryError("MemoryError")
            raise NameError("NameError")
            raise OSError("OSError")
            raise ReferenceError("ReferenceError")
            raise RuntimeError("RuntimeError")
            raise StopAsyncIteration("StopAsyncIteration")
            raise StopIteration("StopIteration")
            raise SyntaxError("SyntaxError")
            raise SystemError("SystemError")
            raise TypeError("TypeError")
            raise ValueError("ValueError")
            raise Warning("Warning")
            raise Exception("Exception")

        """ 

    except ArithmeticError as a:
        print(f"ArithmeticError : 연산자 오류")
        if isinstance(a, FloatingPointError):
            print(f"{a} : 숫자 오류")
        elif isinstance(a, OverflowError):
            print(f"{a} : 넘버 오류")
        elif isinstance(a, ZeroDivisionError):
            print(f"{a} : 분자 오류")
            
    except AssertionError as a:
        print(f"{a} : 테스트 오류")
    except AttributeError as a:
        print(f"{a} : 속성 오류")
    except BufferError as b:
        print(f"{b} : 버퍼 오류")
    except EOFError as e:
        print(f"{e} : 에러 문자열 오류")
        
    except ImportError as i:
        print(f"ImportError : 임포트 오류")
        if isinstance(i, ModuleNotFoundError):
            print(f"{i} : 모듈 오류")
            
    except LookupError as l:
        print(f"LookupError : 참조 범위 오류")
        if isinstance(l, IndexError):
            print(f"{l} : 인덱스 오류")
        elif isinstance(l, KeyError):
            print(f"{l} : 키 오류")
            
    except MemoryError as m:
        print(f"{m} : 메모리 오류")
    except NameError as n:
        print(f"NameError : 이름 오류")
        if isinstance(n, UnboundLocalError):
            print(f"{n} : 로컬 변수 오류")
            
    except OSError as o:
        print(f"OSError : 시스템 오류")
        if isinstance(o, BlockingIOError):
            print(f"BlockingIOError : 블록 오류")
        elif isinstance(o, ChildProcessError):
            print(f"{o} : 자식 프로세스 오류")
        elif isinstance(o, ConnectionError):
            print(f"ConnectionError : 연결 오류")
            if isinstance(o, BrokenPipeError):
                print(f"{o} : 브로큰 파이프 오류")
            elif isinstance(o, ConnectionAbortedError):
                print(f"{o} : 연결 중단 오류")
            elif isinstance(o, ConnectionRefusedError):
                print(f"{o} : 연결 거부 오류")
            elif isinstance(o, ConnectionResetError):
                print(f"{o} : 연결 재설정 오류")
        elif isinstance(o, FileExistsError):
            print(f"{o} : 파일 이미 존재함")
        elif isinstance(o, FileNotFoundError):
            print(f"{o} : 파일 찾을 수 없음")
        elif isinstance(o, IsADirectoryError):
            print(f"{o} : 디렉토리 오류")
        elif isinstance(o, PermissionError):
            print(f"{o} : 권한 오류")
        elif isinstance(o, TimeoutError):
            print(f"{o} : 타임아웃 오류")
            
    except ReferenceError as r:
        print(f"{r} : 참조 오류")
        
    except RuntimeError as r:
        print(f"RuntimeError : 런타임 오류")
        if isinstance(r, NotImplementedError):
            print(f"{r} : 미구현 오류")
        elif isinstance(r, RecursionError):
            print(f"{r} : 재귀 한도 초과 오류")
            
    except StopAsyncIteration as s:
        print(f"{s} : 비동기 순회 종료")
    except StopIteration as s:
        print(f"{s} : 순회 종료")
        
    except SyntaxError as s:
        print(f"SyntaxError : 문법 오류")
        if isinstance(s, IndentationError):
            print(f"IndentationError : 들여쓰기 오류")
            if isinstance(s, TabError):
                print(f"{s} : 탭/공백 혼용 오류")
                
    except SystemError as s:
        print(f"{s} : 시스템 내부 오류")
    except TypeError as t:
        print(f"{t} : 타입 오류")
        
    except ValueError as v:
        print(f"ValueError : 값 오류")
        if isinstance(v, UnicodeError):
            print(f"{v} : 유니코드 오류")
            
    except Warning as w:
        print(f"{w} : 경고 발생")
        
    except Exception as e:
        print(f"{type(e).__name__}: {e} (기타 예외 캐치)")

if __name__ == '__main__':
    exception_hierarchy()