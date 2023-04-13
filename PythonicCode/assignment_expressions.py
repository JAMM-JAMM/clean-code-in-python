import re
from typing import Iterable, Set


ARN_REGEX = re.compile(r"arn:aws:[a-z0-9\-]*:[a-z0-9\-]*:(?P<account_id>\d+):.*")

def collect_account_ids_from_arns(arns: Iterable[str]) -> Set[str]:
    """
    arn:partition:service:region:account-id:resource-id

    형태의 ARN들이 주어진 경우 고유한 계정 ID (account-id)를 찾아서 반환
    """
    collected_account_ids = set()
    for arn in arns:
        matched = re.match(ARN_REGEX, arn)
        if matched is not None:
            account_id = matched.groupdict()['account_id']
            collected_account_ids.add(account_id)
    return collected_account_ids

def collect_account_ids_from_arns2(arns: Iterable[str]) -> Set[str]:
    """
    arn:partition:service:region:account-id:resource-id

    형태의 ARN들이 주어진 경우 고유한 계정 ID (account-id)를 찾아서 반환

    - Comprehension을 사용하여 함수형 프로그래밍과 유사한 방식 그리고 더 적은 코드로 
      동일한 기능을 수행하는 함수 작성
    - matchd_arns는 filter의 결과로 Iterable한 객체
    """
    matched_arns = filter(None, (re.match(ARN_REGEX, arn) for arn in arns))
    return {m.groupdict()["account_id"] for m in matched_arns}

def collect_account_ids_from_arns3(arns: Iterable[str]) -> Set[str]:
    """
    arn:partition:service:region:account-id:resource-id

    형태의 ARN들이 주어진 경우 고유한 계정 ID (account-id)를 찾아서 반환

    - Python 3.8 이상부터 사용할 수 있는 assignment expression을 사용한 방식으로 함수 작성
    - assignment expression은 ':='와 같이 walrus operator를 사용하여 변수의 할당과 반환을
      동시에 할 수 있기 때문에 코드를 간결하게 작성할 수 있음
    """
    return {
        matched.groupdict()["account_id"]
        for arn in arns if (matched := re.match(ARN_REGEX, arn)) is not None
    }