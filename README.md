# 지뢰피하기(Avoid Mines)
## 소개
* 과거에 엑셀로 만들었던 게임을 Python과 pygame 모듈을 활용하여 재현하였다.
* 지뢰찾기(Minesweeper)를 응용하여 마우스가 아닌 키보드로 조작하는 방식.
* 개발 기간 : 2020-09-06 ~ 2020-09-09

## 규칙
* 방향키를 이용하여 이동하며, 시작점에서 도착점까지 도달하면 승리한다.

![7](https://user-images.githubusercontent.com/67459853/92605564-d94b0f00-f2ec-11ea-9cf6-0f7dc6fbdf90.png)

* 지뢰를 밟으면 패배한다.
* 각 칸에는 자기 자신을 중심으로 3x3 정사각형 모양의 공간에 총 몇 개의 지뢰가 매설되어 있는지 숫자로 표시되어 있다.  
  흔히 알고 있는 지뢰찾기(Minesweeper)와는 다르게 주변 8칸뿐 아니라 자기 자신인 중앙 칸까지 계산하여 지뢰의 수를 표시한다.
  
  ![1](https://user-images.githubusercontent.com/67459853/92602684-6db37280-f2e9-11ea-99bc-8885a304b641.PNG)
  
* 게임 시작시 지뢰매설량을 표시하는 숫자는 시작점으로부터 주변 2칸 범위만 공개된다.  

  ![2](https://user-images.githubusercontent.com/67459853/92602758-89b71400-f2e9-11ea-9e0f-680613af8d43.PNG) 
  
  캐릭터를 움직일 때마다 칸을 색칠하여, 지뢰가 없는 안전한 칸임을 표시한다.
  
  ![3](https://user-images.githubusercontent.com/67459853/92603057-d3076380-f2e9-11ea-990c-33db7a1c3e4e.PNG)
  
  캐릭터를 움직일 때마다 이동한 칸의 주변 8칸에 지뢰매설량을 표시하는 숫자를 공개한다.
  
  ![4](https://user-images.githubusercontent.com/67459853/92603099-df8bbc00-f2e9-11ea-8ddd-e8be779f6bee.PNG)
  
* 시작점에서 도착점까지 가는 안전한 최단거리 경로가 반드시 1개 이상 존재한다.
* 시작점 근처에 지뢰가 매설되어 단 한 번의 이동도 없이 50% 확률의 선택을 강요당하는 상황이 발생하지 않도록 시작점 주변 폭탄은 시작시 공개한다.

  ![5](https://user-images.githubusercontent.com/67459853/92603861-c46d7c00-f2ea-11ea-9599-2cf713c172a6.PNG)

## 난이도
* Easy : 전체 칸의 1/5이 지뢰
* Normal : 전체 칸의 1/3이 지뢰
* Hard : 전체 칸의 1/2이 지뢰
* lunatic : 전체 칸의 1/2이 지뢰. 지뢰가 아닌 일부 칸의 숫자가 공개되지 않고 대신 해당 숫자의 홀짝 여부만 공개된다.

![6](https://user-images.githubusercontent.com/67459853/92605244-79546880-f2ec-11ea-9bc3-69d4ba6614a0.PNG)


## 수정해야 할 부분
* 지뢰가 고르게 분포되지 않는 점
* 섬세한 난이도 조절
