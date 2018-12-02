# cloths-classification
simple cloths classification using tensorflow's inception example

---
## filedownload.py
구글에서 이미지를 다운받는 파일입니다. `dest_dir`변수에 파일을 저장할 경로를 지정하고 `keyword`변수에 원하는 검색 키워드를 지정한다.<br>2017년부터 2018년의 사진들을 총 1000장 다운로드 받습니다. 하지만 링크가 깨졌거나 구글에 이미지가 부족하다면 적을 수 있습니다.<br>
`filter`부분의 날짜를 바꾸거나 `max_num`을 바꿔서 다운로드 받을 사진의 갯수를 바꿀 수 있습니다. `max_num`은 1000장 까지 가능합니다. <br>
[icrawler](https://pypi.org/project/icrawler/) 패키지가 필요합니다.

---

## resize.py
원하는 경우 사진의 크기를 바꿔줍니다.<br>
`dirfrom`부분에 원본 사진들이 저장된 경로를, `dirto`부분에 크기가 변경된 사진들의 경로를 적어줍니다.<br>
`im.resize`뒤의 값을 바꿔 원하는 크기를 바꿀 수 있습니다.<br>
[pillow](https://pypi.org/project/Pillow/)패키지가 필요합니다.

---

---
## 학습

---
### 데이터
사진을 저장할 디렉토리를 만들고, 하위에 분류할 라벨별로 디렉토리를 생성합니다.<br>
filedownload.py를 사용하여 원하는 라벨별로 분류된 디렉토리에 각각 사진을 받습니다.<br>
사진을 확인하여 불필요한 파일을 제거합니다.<br>
<br>

### retrain.py
학습을 진행하는 파일입니다. [tensorflow](https://github.com/tensorflow/tensorflow)의 inception v3 예제 파일입니다. 다음의 명령을 사용하여 학습을 시작합니다.
```bash
python retrain.py --bottleneck_dir=./bottlenecks --how_many_training_steps 500 --model_dir=./inception --output_graph=./retrained_graph.pb --output_labels=./retrained_labels.txt --image_dir ./dataset
```
* --bottleneck_dir bottleneck 파일들이 생성될 경로
* --how_many_training_steps training 횟수
* --model_dir 모델이 생성될 경로
* --output_graph 생성된 그래프 파일.
* --output_labels 생성된 라벨 텍스트 파일.
* --image_dir 이미지들이 위치한 폴더

### label_image.py
학습이 종료된 후 retrained_graph.pb와 retrained_labels.txt가 생성된 경로에서 실행하면 결과를 알려줍니다.<br>
이 파일 또한 [tensorflow](https://github.com/tensorflow/tensorflow)의 예제 파일입니다.
<br>다음의 명령을 통해 결과를 확인합니다.
```bash
python label_image.py --image 000003.jpg --graph retrained_graph.pb --labels retrained_labels.txt --input_layer=Placeholder --output_layer=final_result
```
* --image 테스트 할 이미지 파일입니다.
* --graph 추정에 사용할 그래프입니다. 학습 후 생성된 .pb파일을 사용하세요.
* --labels 추정에 사용할 label입니다. 학습 후 생성된 .txt파일을 사용하세요.
* --input_layer 그대로 사용하세요.
* --output_layer 그대로 사용하세요.

## google colab 에서 사용
예제를 구글 colab에서 사용하기 위한 방법입니다.<br>
구글에 로그인하고 [google colab](https://colab.research.google.com/)에 들어가서 새 python3 노트를 생성합니다.

### 데이터셋 업로드
왼쪽의 > 버튼을 누르고 파일 탭을 선택하여 런타임에 연결합니다.<br>
왼쪽 상단의 +code버튼을 눌러 다음의 코드를 추가합니다.
```bash
mkdir data
mkdir data/Downjacket
mkdir data/Coat
mkdir data/Shirt
mkdir data/Sweater
```
위의 코드는 data라는 디렉토리를 만들고 그 안에 네개의 디렉토리를 만듭니다. 상황에 맞게 수정해서 사용하세요.<br>
Ctrl+Enter를 누르면 실행됩니다.<br>
파일 탭에서 새로고침을 눌렀을때 디렉토리가 잘 생성되었다면 각각의 디렉토리를 우클릭하고 업로드를 눌러 사진들을 업로드 합니다. <br>
업로드는 디렉토리 별로 진행해야 합니다.

### 학습, 추정 코드 업로드
파일 탭에서 업로드를 눌러 retrain.py와 label_image.py를 업로드 해 주세요.<br>
파일탭의 새로고침을 눌러 파일들이 업로드 된 것을 확인해주세요.

### 학습
GPU를 사용하여 빠르게 학습하고 싶다면 메뉴의 런타임 탭에서 런타임 유형 변경을 눌러 하드웨어 가속기를 GPU로 바꿔주세요.<br>
+코드 버튼을 눌러 다음의 코드를 추가합니다.
```bash
!python retrain.py --bottleneck_dir=./bottlenecks --how_many_training_steps 500 --model_dir=./inception --output_graph=./retrained_graph.pb --output_labels=./retrained_labels.txt --image_dir ./data
```
Ctrl+Enter를 눌러 실행합니다. 학습을 실행하고 진행결과가 출력됩니다.

### 확인
파일탭에서 업로드를 눌러 
추정에 사용할 이미지를 업로드 하세요.
+코드 버튼을 눌러 다음의 코드를 추가합니다.
```bash
!python label_image.py --image .jpg --graph retrained_graph.pb --labels retrained_labels.txt --input_layer=Placeholder --output_layer=final_result
```
.jpg 앞부분에 방금 업로드한 이미지의 이름을 적고 Ctrl+Enter를 눌러 실행합니다. 각 라벨에 대한 예측치가 크기순으로 정렬되어 출력됩니다!
