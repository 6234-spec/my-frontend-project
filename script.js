window.onload = function () {
  var merrywrap = document.getElementById("merrywrap");
  var box = merrywrap.getElementsByClassName("giftbox")[0];
  var step = 1;
  var stepMinutes = [2000, 2000, 1000, 1000];

  function init() {
    box.addEventListener("click", openBox, false);
  }

  function stepClass(step) {
    merrywrap.className = 'merrywrap';
    merrywrap.className = 'merrywrap step-' + step;
  }

  function openBox() {
    if (step === 1) {
      box.removeEventListener("click", openBox, false);
    }

    stepClass(step);

    // 关键：step=3 时发送请求触发 Python 弹窗（核心修改部分）
    if (step === 3) {
      // 向本地 Flask 服务器发送请求，触发 Python 脚本
      fetch('http://localhost:5000/run-popup')
        .then(response => {
          if (!response.ok) {
            console.log('请求成功但服务器返回异常');
          }
        })
        .catch(err => console.log('Python 弹窗调用失败：', err));
    }

    if (step === 4) {
      return;
    }

    setTimeout(openBox, stepMinutes[step - 1]);
    step++;
  }

  init();
};