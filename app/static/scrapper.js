const download_btn = document.querySelector("#telegraph-download-btn")
const list_of_urls = document.querySelector("#urls_list")
download_btn.addEventListener("click", start_download)
const saveFile = (blobURL, filename) => {
  const a = document.createElement('a');
  a.href = blobURL;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
};
async function start_download(){
  download_btn.disabled = true
  download_btn.classList.add("is-loading")
  try {
    let urls = list_of_urls.value.trim().split("\n")
    const response = await fetch("/api/scrapper", {
      method: "post",
      body: JSON.stringify({ urls }),
      headers: {
        "Content-Type": "application/json",
      },
    })
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const blob = await response.blob()
    const blobURL = URL.createObjectURL(blob)
    const now = new Date()

    saveFile(blobURL, `archive-${now.getMilliseconds()}.zip`)
    URL.revokeObjectURL(blobURL)
  } finally {
    download_btn.disabled = false
    download_btn.classList.remove("is-loading")
  }
}