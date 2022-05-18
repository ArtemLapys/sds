function hex_to_buffer(string) {
	let resString = [];
	for (let i = 0; i < string.length; i += 2) {
		resString.push(string.slice(i, i + 2));
	}
	string = resString;
	return string
		.filter(function (chr) {
			return chr !== "";
		})
		.map(function (chr) {
			return parseInt(chr, 16);
		});
}

function loadContentPost() {
	const http = new XMLHttpRequest();
	http.onreadystatechange = function () {
		// Проверим, пришел ли запрос - 200 запрос прошел. === - проверка и по значению и по типу. Они должны быть равны
		if (this.readyState === 4 && this.status === 200) {
			// Получаем данные из запроса
			data = encodeURIComponent(this.response);

			data = hex_to_buffer(data);
			// console.log(data);
			let content = msgpack.decode(data);

			// console.log("Вывод");
			// console.log(content);

			content = JSON.parse(content);
			let html = "";

			for (let i = 0; i < content.length; i++) {
				const fields = content[i].fields;

				let dateCreate = new Date(
					fields.time_create_post.slice(0, fields.time_create_post.indexOf("."))
				);

				date = `${dateCreate.getDate()}.${
					dateCreate.getMonth() + 1 > 10
						? dateCreate.getMonth() + 1
						: "0".concat(dateCreate.getMonth() + 1)
				}.${dateCreate.getFullYear()}`;
				time = `${dateCreate.getHours()}:${dateCreate.getMinutes()}`;

				let dateEdit = new Date(
					fields.time_edit_post.slice(0, fields.time_edit_post.indexOf("."))
				);

				dateEd = `${dateEdit.getDate()}.${
					dateEdit.getMonth() + 1 > 10
						? dateEdit.getMonth() + 1
						: "0".concat(dateEdit.getMonth() + 1)
				}.${dateEdit.getFullYear()}`;
				timeEd = `${dateEdit.getHours()}:${dateEdit.getMinutes()}`;

				html += `	 <h1 class="headPostTitle">${fields.title}</h1>
						<p class="dataTimePost">
							<span class="timePost">🕙 ${time}</span>
							<span class="datePost">📅 ${date}</span>
						</p>
						
						<div class="mainText">${fields.content}
						</div>
						<div class="imgPost">`;

				if (fields.image != "") {
					html += `<img class="mainImagePost" src="../../media/${fields.image}"></div>`;
				}
				if (fields.time_create_post != fields.time_edit_post) {
					
					html += `<p class="dataTimeEditPost">📝Поледний раз пост был отредактирован ${dateEd} в ${timeEd}.</p>`;
				}
			}
			document.getElementById("content").innerHTML = html;
		}
	};
	const post_id = document.location.pathname.slice(6).split("-")[0];
	http.open("GET", `../../api/msgpack-post/${post_id}`, true);
	console.log(`../../api/msgpack-post/${post_id}`);
	http.send();
}

loadContentPost();
