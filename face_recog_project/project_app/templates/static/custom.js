function navSlide() {
    const burger = document.querySelector(".burger");
    const nav = document.querySelector(".nav-links");
    const navLinks = document.querySelectorAll(".nav-links li");
    
    burger.addEventListener("click", () => {
        //Toggle Nav
        nav.classList.toggle("nav-active");
        
        //Animate Links
        navLinks.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = ""
            } else {
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.5}s`;
            }
        });
        //Burger Animation
        burger.classList.toggle("toggle");
    });
    
}

navSlide();



// function([string1, string2],target id,[color1,color2])    
consoleText(['Face recognition AI app', 'Easily Get Criminal Record', 'Get Personal Information',], 'text',['white','wheat','wheat']);

function consoleText(words, id, colors) {
  if (colors === undefined) colors = ['#fff'];
  var visible = true;
  var con = document.getElementById('console');
  var letterCount = 1;
  var x = 1;
  var waiting = false;
  var target = document.getElementById(id)
  target.setAttribute('style', 'color:' + colors[0])
  window.setInterval(function() {

    if (letterCount === 0 && waiting === false) {
      waiting = true;
      target.innerHTML = words[0].substring(0, letterCount)
      window.setTimeout(function() {
        var usedColor = colors.shift();
        colors.push(usedColor);
        var usedWord = words.shift();
        words.push(usedWord);
        x = 1;
        target.setAttribute('style', 'color:' + colors[0])
        letterCount += x;
        waiting = false;
      }, 1000)
    } else if (letterCount === words[0].length + 1 && waiting === false) {
      waiting = true;
      window.setTimeout(function() {
        x = -1;
        letterCount += x;
        waiting = false;
      }, 1000)
    } else if (waiting === false) {
      target.innerHTML = words[0].substring(0, letterCount)
      letterCount += x;
    }
  }, 120)
  window.setInterval(function() {
    if (visible === true) {
      con.className = 'console-underscore hidden'
      visible = false;

    } else {
      con.className = 'console-underscore'

      visible = true;
    }
  }, 400)
}








$(function(){
  $(document).keypress(function(e) {
    cwrite(e.which,'Keypress event');
    if(e.which==120) custom_dialog_toggle('Keypress x','You opened this window by pressing x');
  });
});

//upload
function custom_dialog_toggle(title,text,buttons) {
  if(typeof title !=='undefined') $('#dlg-header').html(title);
  if(typeof text !=='undefined') $('#dlg-content').html(text);
  cwrite('Current state: '+$('#dialog_state').prop("checked"),'custom_dialog_toggle');
  $('#dialog_state').prop("checked", !$('#dialog_state').prop("checked"));
}


//webcam
function custom_dialog_toggle(title,text,buttons) {
  if(typeof title !=='undefined') $('#dlg-header').html(title);
  if(typeof text !=='undefined') $('#dlg-content').html(text);
  cwrite('Current state: '+$('#dialog_state1').prop("checked"),'custom_dialog_toggle');
  $('#dialog_state1').prop("checked", !$('#dialog_state1').prop("checked"));
}


// Console logging function for debugging
// cwrite(str, title)
//      str:              string to be appended to console
//      title (optional): title of the string
// (c)  Tuomas Hatakka 2015
//      http://tuomashatakka.fi
function cwrite(str,title) {
  var ce = $('#console');
  var sg = "<p>";
  if(typeof title !=='undefined') sg = sg+"<em>"+title+"</em> ";
  sg = sg+str+"</p>";
  ce.prepend(sg);
  //if(ce.children("p").length>6) ce.children("p").first().remove();
}







