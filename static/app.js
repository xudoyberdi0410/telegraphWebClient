Filevalidation = () => {
	const fi = document.getElementById('images');
	// Check if any file is selected.
	if (fi.files.length > 0) {
		for (let i = 0; i <= fi.files.length - 1; i++) {
 
			const fsize = fi.files.item(i).size;
			const file = Math.round((fsize / 1024));
			// The size of the file.
			if (file >= 5120) {
				alert(
				  `Файл ${fi.files.item(i).name} слишком большой! Файл должен быть менее 5 МБ`);
				fi.value = ""
			}
		}
	}
}
document.querySelector('#form').onsubmit = () => {
	document.querySelector('#loader').classList.remove('hidden')
}