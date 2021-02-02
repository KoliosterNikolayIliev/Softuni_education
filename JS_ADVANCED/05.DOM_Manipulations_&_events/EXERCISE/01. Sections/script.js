function create(words) {
   let mainDiv = document.getElementById('content')
   mainDiv.addEventListener('click', unHide)
   for (let word of words){
      let p = document.createElement('p')
      p.textContent = word
      p.style.display = 'none'
      let div = document.createElement('div')
      div.appendChild(p)
      mainDiv.appendChild(div)

   }
   function unHide(event){
      if (event.target.tagName === 'DIV' && event.target.className === ''){
         let show = event.target.children[0].style
         if (show.display === 'none'){
            show.display = ''
         }else{
            show.display = 'none'
         }
         console.log('unhide');
      }

   }
}