document.addEventListener("keyup",(e)=>{
 if(e.target.matches(".filtro-cartas")){
  document.querySelectorAll(".carta").forEach((tarjeta)=>{
   tarjeta.textContent.toLocaleLowerCase().includes(e.target.
   value)
     ?tarjeta.classList.remove("filter")
     :tarjeta.classList.add("filter");
    });
    }
   });

   