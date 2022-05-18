
var nextItem = 0
var count = 5;

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

		if (this.readyState === 4 && this.status === 200) {




			data = encodeURIComponent(this.response)
		
			data = hex_to_buffer(data)
			// console.log(data)
			let content = msgpack.decode(data);

			// console.log("Вывод")
			// console.log(content)
			
			content = JSON.parse(content)
			let html = "";

			
			for (let i = 0; i < content.length; i++) {
				const fields = content[i].fields;
				// console.log(fields.title)
				let date = new Date(fields.time_create_post.slice(0, fields.time_create_post.indexOf('.')));
				
				date = `${date.getDate()}.${date.getMonth()+1 > 10 ? date.getMonth()+1 : '0'.concat(date.getMonth()+1)}.${date.getFullYear()} ${date.getHours()}:${date.getMinutes()}`;
				
				html += `<a href="./post/${content[i].pk}-${fields.slug}">
				<li>
					<div class="post">
						<div class="img__post">\n`;

				if (fields.image !== "") {
					html += `<img class="image__post" src="/media/${fields.image}">\n`;
				}
				html += `</div>
						<div class="text__post">
							<div class="content__post">
							<h1 class="headPostTitle">${fields.title}</h1>
							<p class="dataPost">${date}</p>                   
							<p class="headPostContent">${fields.content.replace(/(?:\\[rn])+/g, "").split(' ').filter( str => str != '').slice(0, 65).join(' ')} ...</p>
						</div>
					</div>
				</div>
				</li>
			</a>`;
			}
			document.getElementById('content').innerHTML = html;
		}
	};
	
	http.open("GET", `./api/msgpack/${nextItem}`, true);
	nextItem += count;
	http.send();
	
}
loadContentPost();

var checkScroll = function () {
	if (
		document.body.scrollTop + document.body.clientHeight + 100 >= document.body.scrollHeight
	) {
		loadMore();
	}
};

function loadMore() {

	const http = new XMLHttpRequest();
	http.open("GET", `./api/msgpack/${nextItem}`, false);
	http.send();


	if (http.readyState === 4 && http.status === 200) {

		data = encodeURIComponent(http.response);
		// console.log(data)


		data = hex_to_buffer(data);
		content = msgpack.decode(data);
		content = JSON.parse(content);


		if (content.length == 0) {
			document.removeEventListener("scroll", checkScroll);
		}
		for (let i = 0; i < content.length; i++) {
			let html = "";
			const fields = content[i].fields;
			let date = new Date(
				fields.time_create_post.slice(0, fields.time_create_post.indexOf("."))
			);

			date = `${date.getDate()}.${
				date.getMonth() + 1 > 10
					? date.getMonth() + 1
					: "0".concat(date.getMonth() + 1)
			}.${date.getFullYear()} ${date.getHours()}:${date.getMinutes()}`;

			html += `<a href="./post/${content[i].pk}-${fields.slug}">
				<li>
					<div class="post">
						<div class="img__post">\n`;

			if (fields.image !== "") {
				html += `<img class="image__post" src="/media/${fields.image}">\n`;
			}
			html += `</div>
						<div class="text__post">
							<div class="content__post">
							<h1 class="headPostTitle">${fields.title}</h1>
							<p class="dataPost">${date}</p>                   
							<p class="headPostContent">${fields.content
								.replace(/(?:\\[rn])+/g, "")
								.split(" ")
								.filter((str) => str != "")
								.slice(0, 65)
								.join(" ")} ...</p>
						</div>
					</div>
				</div>
				</li>
			</a>`;
			document.getElementById("content").innerHTML += html;
		}
	}

	nextItem += count;
}

const main = document.getElementById("main_news");
document.addEventListener("scroll", checkScroll);

