var arr = [];

function clickBtn(id) {
	if (id == 0) {
		// Math.random() : 0 ~ 1 사이의 난수 생성
		// Math.floor() : 해당 숫자와 같거나 작은 정수 중 가장 큰 수 반환
		var randomNum0 = Math.floor(Math.random() * 99 + 1); // 1 ~ 100 사이의 난수 생성
		arr.push(randomNum0);

		// 해당 HTML element 에 난수값 출력
		document.getElementById("area1").innerHTML = randomNum0;
	} else if (id == 1) {
		const randomNum1 = Math.floor(Math.random() * 99 + 1); // 1 ~ 100 사이의 난수 생성
		arr.push(randomNum1);

		// 해당 HTML element 에 난수값 출력
		document.getElementById("area2").innerHTML = randomNum1;
	} else {
		const randomNum2 = Math.floor(Math.random() * 99 + 1); // 1 ~ 100 사이의 난수 생성
		arr.push(randomNum2);

		// 해당 HTML element 에 난수값 출력
		document.getElementById("area3").innerHTML = randomNum2;
	}
}

function resultBtn() {
	result = "";

	if (arr.length === 3) {
		// 난수들을 문자열 형태로 꺼내왔으므로 parseInt (문자열 -> 정수 변환)
		sum = arr[0] + arr[1] + arr[2];
		result += `총합은 ${sum} 입니다!`;
		document.getElementById("result").innerHTML = result;
	} else {
		alert("모든 난수를 입력해주세요!");
	}
}

function imgBtn() {
	var gameElement = document.getElementById("game");
	var btnElement = document.getElementById("img");
	var textElement = document.getElementById("startText");

	btnElement.style.display = "none";
	textElement.style.display = "none";
	gameElement.style.display = "block";
}

function changeStop(box) {
	box.setAttribute("src", "../../../static/image/stopbox.png");
}

function changeMove(box) {
	box.setAttribute("src", "../../../static/image/box.gif");
}
