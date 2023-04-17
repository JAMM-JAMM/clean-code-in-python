"""
Connector 객체는 source 파라미터를 사용해 생성되며,
source와 timeout이라는 2개의 속성을 갖는다.
source는 publice이며, timeout은 private이다.

단일 밑줄을 접두사로 사용하는 것은 객체의 인터페이스를 명확하게 구분하는 파이썬스러운 방식이다.

_timeout은 connector 자체에서만 사용되고 호출자는 이 속성에 접근하지 않아야 한다.
즉, timeout 속성은 내부에서만 사용하고 바깥에서는 호출하지 않을 것이므로 외부 인터페이스를 고려하지 않고
언제든 안전하게 리팩토링할 수 있다.

클래스는 외부 호출 객체와 관려된 속성과 메서드만을 노출해야 한다.
즉, 객체의 인터페이스로 공개하는 용도가 아니라면 모든 멤버는 접두사로 하나의 밑줄을 사용하는 것이 좋다.

밑줄로 시작하는 속성은 private처럼 취급되어야 하고 외부에서 호출하면 안 된다.
"""

class Connector:
    def __init__(self, source):
        self.source = source
        self._timeout = 60

if __name__ == '__main__':
    conn = Connector("postgresql://localhost")
    print(conn.source)
    print(conn._timeout)
    print(conn.__dict__)