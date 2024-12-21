// const uploadDiv = document.getElementById('uploadDiv');
//         const fileInput = document.getElementById('fileInput');

        // uploadDiv.addEventListener('click', () => {
        //     fileInput.click(); // Programmatically trigger the file input
        // });

        // fileInput.addEventListener('change', (event) => {
        //     const file = event.target.files[0];
        //     // if (file) {
        //     //     alert(`File selected: ${file.name}`);
        //     // }
        // });
const selectImage = document.querySelector('#uploadDiv');
const inputFile = document.querySelector('#fileInput');
const imgArea = document.querySelector('.img-area');
const submit=document.querySelector('.btn')
// submit.addEventListener('click',function(event){
//     event.preventDefault();
// })
        
selectImage.addEventListener('click', function () {
        inputFile.click();
    })
        
inputFile.addEventListener('change', function () {
    const image = this.files[0]
        if(image.size < 2000000) {
            const reader = new FileReader();
                reader.onload = ()=> {
                    const allImg = imgArea.querySelectorAll('img');
                    allImg.forEach(item=> item.remove());
                    const imgUrl = reader.result;
                    const img = document.createElement('img');
                    img.src = imgUrl;
                    imgArea.appendChild(img);
                    imgArea.classList.add('active');
                    imgArea.dataset.img = image.name;
                }
                reader.readAsDataURL(image);
            } else {
                alert("Image size more than 2MB");
            }
        })
document.addEventListener('DOMContentLoaded', function() {
            const colorBoxes = document.querySelectorAll('.color-box');
            colorBoxes.forEach(box => {
                box.addEventListener('click', function() {
                    const color = this.getAttribute('data-color');
                    navigator.clipboard.writeText(color).then(() => {
                        console.log('Color code copied to clipboard: ' + color);
                    }).catch(err => {
                        console.error('Error copying text: ', err);
                    });
                });
            });
        });
