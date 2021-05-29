# Python-HTML-Parser

## 개요

beautifulsoup으로는 만족못해서 만들어보는 Python3.9 버전의 HTML 파싱기

~를 구현해보는 개인 프로젝트입니다.

## 목적성

### 프로젝트 목표

javascript에서 제공하는 `document.querySelector()` 메소드를 파이썬 상에서 구현하는 것이 목표이며,

그 외에도 간단한 Document Object Model(DOM)을 생성하고 수정이 가능한 parser를 구현하는 것 입니다.

### 개인 목표

본 프로젝트를 수행하며 개인적으로 성취하고자 하는 것에는 다음과 같은 것들이 있습니다.

1. [Google의 python style guide](https://google.github.io/styleguide/pyguide.html)를 통해 가독성이 좋고 정형화된 naming convention 사용하기.
1. 꼼꼼한 doc-string 작성으로 타인이 사용하기 편한 형태의 API 작성에 익숙해지기.
1. unittest를 직접 작성해보고 모듈단위의 테스팅에 익숙해지기.
1. GitHub를 능숙하게 사용하기.
    - GitFlow를 통해 git graph를 깔끔하게 유지하고, 향후 bug tracking 혹은 프로젝트 개발 역사 정리가 수월하도록 하기.
    - Pull Request 방법에 익숙해지기.
        - 모듈, 기능 등의 단위로 개발하여 pr을 하는 방법으로, branch 분기를 체계화 하기
        - merge / squash and merge / rebase 등 다양한 merge 방법들을 시험해보며, 장단점 비교해보며 익숙해지기.
        - Codacy를 통해 코딩 스타일을 객관적으로 검토해보기.
    - Issue/PR 를 생성하며 현재 작업 중인 내용을 일관성있게 유지·관리하기


## 구현

본 프로젝트의 구현은 w3.org에 명세된 [Document Object Model (Core) Level 1](https://www.w3.org/TR/REC-DOM-Level-1/level-one-core.html) 를 참조하여 이루어지고 있습니다.

각 인터페이스의 property와 method들은 python의 개발 철학에 맞추어 이름을 변경하기도 하였습니다.

예:

Javascript API:
```javascript
Node.childNodes()
```

Python API(본 프로젝트):
```python
Node.child_nodes()
```


