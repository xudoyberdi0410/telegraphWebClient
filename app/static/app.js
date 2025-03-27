window.onload = () => {
  const name = localStorage.getItem("name") || "";
  const username = localStorage.getItem("username") || "";
  const boosty_auth = localStorage.getItem("boosty_auth") || "";

  document.querySelector("#boosty_input").value = boosty_auth;
  document.querySelector("#name").value = name;
  document.querySelector("#username").value = username;
};

function publish_click() {
  let name = document.querySelector("#name").value;
  let username = document.querySelector("#username").value;
  localStorage.setItem("name", name);
  localStorage.setItem("username", username);
}
document.querySelector("form").addEventListener("submit", function (event) {
  event.preventDefault();
  let name = document.querySelector("#name").value;
  let username = document.querySelector("#username").value;
  let link = document.querySelector("#teletype_url").value;

  let button = document.querySelector("#btn");
  button.classList.add("is-loading");
  // let newurl = document.querySelector("#new_url");
  let body = {
    name: name,
    username: username,
    link: link,
  };
  if (localStorage.getItem("boosty_auth")){
	body.boosty_auth = localStorage.getItem("boosty_auth")
  }
  fetch("/api", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  })
    .then((response) => response.json())
    .then((data) => {
      button.classList.remove("is-loading");
      new_message("success", `<a href="${data.url}">${data.url}</a>`)
    })
	.catch(error => {
		button.classList.remove("is-loading");
    console.log("ERRRR");
    
    new_message("error", "Couldn't create a article! Try again later!")
		// Optionally, display error to the user
	});
});
document.querySelector("#settings-btn").onclick = (e) => {
  document.querySelector("#settings-menu").classList.add("is-active");
};

document.querySelector("button.delete").onclick = (e) =>
  document.querySelector("#settings-menu").classList.remove("is-active");

document.querySelector("#save-settings").onclick = (e) => {
  let boosty_auth = document.querySelector("#boosty_input").value;
  localStorage.setItem("boosty_auth", boosty_auth);
};
document.querySelector("#cancel-settings").onclick = (e) => {
  let boosty_auth = "";
  if (localStorage.getItem("boosty_auth")) {
    boosty_auth = localStorage.getItem("boosty_auth");
  }
  document.querySelector("#boosty_input").value = boosty_auth;
  document.querySelector("#settings-menu").classList.remove("is-active");
};

function new_message(type, message){
  let main_block = document.querySelector("#main-block")
  switch (type) {
    case "success":
      main_block.insertAdjacentHTML("beforeend", 
        `<article class="message py-1 is-success">
            <div class="message-header">
              <p>Success</p>
              <button class="delete" aria-label="delete" onclick="removeMessage(this)"></button>
            </div>
				    <div class="message-body">
              ${message}
            </div>
        </article>`
			)
      break;
    case "error":
      main_block.insertAdjacentHTML("beforeend", 
        `<article class="message py-1 is-danger">
            <div class="message-header">
              <p>Error</p>
              <button class="delete" aria-label="delete" onclick="removeMessage(this)"></button>
            </div>
				    <div class="message-body">
              ${message}
            </div>
        </article>`
      )
      break;
    default:
      break;
  }
}
function removeMessage(element) {
  element.closest('.message').remove();
}