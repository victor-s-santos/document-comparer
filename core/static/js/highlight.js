highlight($("#new"), $("#old"));

function highlight(newElem, oldElem){ 
  var oldText = oldElem.text(),     
      text = '',
      spanOpen = false;  
  newElem.text().split('').forEach(function(val, i){  
    if (val != oldText.charAt(i)){   
      text += !spanOpen ? "<span class='highlight'>" : "";
      spanOpen = true;
    } else {       
      text += spanOpen ? "</span>" : "";
      spanOpen = false;  
    }  
    text += val;
  });
  newElem.html(text); 
}

.highlight {background-color: #B4D5FF}
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
<p id="old">this is number 123</p>
<p id="new">that is number 124</p>