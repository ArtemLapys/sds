var nextItem = 0
var count = 5;

function unpack(str) {
    var bytes = [];
    for(var i = 0; i < str.length; i++) {
        var char = str.charCodeAt(i);
        bytes.push(char >>> 8);
        bytes.push(char & 0xFF);
    }
    return bytes;
}

function loadContentPost() {
	
	const http = new XMLHttpRequest();
	http.onreadystatechange = function () {
		// Проверим, пришел ли запрос - 200 запрос прошел. === - проверка и по значению и по типу. Они должны быть равны
		if (this.readyState === 4 && this.status === 200) {
			// Получаем данные из запроса
			// console.log(this.responseText)


			var bytes = []; // char codes

			for (var i = 0; i < this.responseText.length; ++i) {
			var code = this.responseText.charCodeAt(i);

			bytes = bytes.concat([code]);
			}
			// var uint8 = new Uint8Array(bytes)
			
			// for (var i = 0; i < input.length; i++) {
      		// 	output.value += input[i].charCodeAt(0).toString(2) + " ";
  			// }
			var test = new Uint8Array(bytes)
			const content = msgpack.deserialize(test, {multiple:true});
			console.log(bytes)
			let html = "";
			console.log(content)
			
			// console.log(typesof(content))


			
			for (let i = 0; i < content.length; i++) {
				const fields = content[i].fields;
				console.log(fields.title)
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
	
	http.open("GET", `./api/msgpack/`, true);
	nextItem += count;
	http.send();
	
}
loadContentPost();



// var checkScroll =  function() {
//   if (document.body.scrollTop +document.body.clientHeight+100 >= document.body.scrollHeight) {
//     loadMore();
//   }
// }

// function loadMore() {
// const http = new XMLHttpRequest();
// 	http.open("GET", `./api/json/${nextItem}`, false);
// 	http.send();

// 		// Проверим, пришел ли запрос - 200 запрос прошел. === - проверка и по значению и по типу. Они должны быть равны
// 		if (http.readyState === 4 && http.status === 200) {
// 			// Получаем данные из запроса
			
// 			const content = JSON.parse(http.responseText);
// 			if (content.length == 0){
// 				document.removeEventListener('scroll', checkScroll)
// 			}
// 			for (let i = 0; i < content.length; i++) {
// 				let html = "";
// 				const fields = content[i].fields;
// 				let date = new Date(fields.time_create_post.slice(0, fields.time_create_post.indexOf('.')));
				
// 				date = `${date.getDate()}.${date.getMonth()+1 > 10 ? date.getMonth()+1 : '0'.concat(date.getMonth()+1)}.${date.getFullYear()} ${date.getHours()}:${date.getMinutes()}`;
				
// 				html += `<a href="./post/${content[i].pk}-${fields.slug}">
// 				<li>
// 					<div class="post">
// 						<div class="img__post">\n`;

// 				if (fields.image !== "") {
// 					html += `<img class="image__post" src="/media/${fields.image}">\n`;
// 				}
// 				html += `</div>
// 						<div class="text__post">
// 							<div class="content__post">
// 							<h1 class="headPostTitle">${fields.title}</h1>
// 							<p class="dataPost">${date}</p>                   
// 							<p class="headPostContent">${fields.content.replace(/(?:\\[rn])+/g, "").split(' ').filter( str => str != '').slice(0, 65).join(' ')} ...</p>
// 						</div>
// 					</div>
// 				</div>
// 				</li>
// 			</a>`;
// 			document.getElementById('content').innerHTML += html;
// 			}
// 		}
	
// 	nextItem += count;
	
// } 

// const main = document.getElementById('main_news')
// document.addEventListener('scroll', checkScroll);




// ${date.toLocaleString('default', { month: 'long' } - месяц текстом










