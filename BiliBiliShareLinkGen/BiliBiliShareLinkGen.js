var xhr = new XMLHttpRequest();
xhr.open("POST", 'https://api.bilibili.com/x/share/click', true);

xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

xhr.onreadystatechange = function() {
    if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
        alert(JSON.parse(xhr.response).data.content);
    }
}

xhr.send("build=1&buvid=2s5d136975d5f8d4528f254d53845s2d&platform=windows&oid=" + aid + "&share_channel=COPY&share_id=main.ugc-video-detail.0.0.pv&share_mode=1");