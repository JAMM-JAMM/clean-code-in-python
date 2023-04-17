"""
Connector 객체에서 timeout 속성을 이중 밑줄로 정의했다고 가정해보자.

외부에서 __timeout에 접근하려고 할 때 발생하는 예외를 살펴보면,
AttributeError 에러로 속성이 존재하지 않는다고 말하며
"이것은 private이다" 또는 "이것은 접근할 수 없다"는 식으로 말하지 않고
단지 그것은 존재하지 않는다고 말한다. 이것은 실제로 뭔가 다른 일이 벌어졌으며
부작용에 의한 결과로 생긴 것이라는 것을 암시한다.
"""

class Connector:
    def __init__(self, source):
        self.source = source
        self.__timeout = 60
    
    def connect(self):
        print("connecting with {0}s".format(self.__timeout))

if __name__ == "__main__":
    conn = Connector("postgresql://localhost")
    print(conn.connect)
    # print(conn.__timeout) # AttributeError

    """
    밑줄 두 개를 사용하면 파이썬은 다른 이름을 만든다.
    "name mangling"이라는 것으로 이것이 하는 일은
    이중 밑줄을 사용한 변수의 이름을 "_<class_name>__<attribute-name>" 형태로 변경하는 것이다.
    해당 예제에서는 "_Connector_timeout"이라는 속성이 만들어지며 이 속성은 변경된 속성으로 접근할 수 있다.

    파이썬에서 이중 밑줄을 사용하는 것은 완전히 다른 경우를 위한 것이다.
    여러 번 확장되는 클래스의 메서드를 이름 충돌 없이 오버라이드하기 위해 만들어졌기 때문에,
    이중 밑줄을 사용하는 것은 파이썬스러운 코드가 아니며 속성을 private으로 정의하려는 경우에는
    하나의 밑줄을 사용하고 파이썬스러운 관습을 지키도록 해야 한다.
    """

    print(vars(conn)) # {'source': 'postgresql://localhost', '_Connector__timeout': 60}
    print(conn._Connector__timeout)
    
    conn._Connector__timeout = 30
    print(conn._Connector__timeout)
    print(conn.connect())