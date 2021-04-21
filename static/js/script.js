var imgPath ='-'

function myFunction(imgs) {
  imgPath = imgs.src;
  dispPage();
}
function dispPage() {
  var cb1 = document.getElementById("corner");
  var cb2 = document.getElementById("reconstruct");
  var clr = document.getElementById("myDropdown").selectedIndex;
  var reconsImg = document.getElementById("reconsImg");
  var expandImg = document.getElementById("expandedImg");
  var imgText = document.getElementById("imgtext");
  console.log(imgPath)
  if(imgPath == '-'){
    expandImg.src = '/data/bg.png';
    console.log(imgPath);
    expandImg.parentElement.style.display = "block";
  }
  else{
      console.log(imgPath);
      var pathArr = imgPath.split("/");
      var imPath = '';
      for(var i=0;i <pathArr.length-1;i++){
         imPath=imPath.concat(pathArr[i]);
         imPath=imPath.concat('/');
      }
      var imName = pathArr[pathArr.length-1].split('.png')[0];
      if (cb1.checked == true){
        var canvIm = imPath.concat('TV_').concat(imName).concat('.png');
      }else {
         var canvIm = imPath.concat(imName).concat('.png');
      }
      expandImg.src = canvIm;
      if (cb2.checked == true){
          if(clr==1){
              var canvIm = imPath.concat('per_').concat(imName).concat('.png');
          }
          else if(clr==2){
              var canvIm = imPath.concat('qual_').concat(imName).concat('.png');
          }
          else{
              var canvIm = imPath.concat('grey_').concat(imName).concat('.png');
          }
            reconsImg.src = canvIm;
            reconsImg.parentElement.style.display = "block";
      }else {
         reconsImg.src = '';
         reconsImg.parentElement.style.display = "none";
      }
      expandImg.parentElement.style.display = "block";
  }
}

function getCredit() {
  var x = document.getElementById("credit");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

 // To download csv
function getCSV() {
  var pathArr = imgPath.split("/");
  var imPath = '';
  for(var i=0;i <pathArr.length-1;i++){
     imPath=imPath.concat(pathArr[i]);
     imPath=imPath.concat('/');
  }
  var imName = pathArr[pathArr.length-1].split('.png')[0];
  var canvIm = imPath.concat('data_').concat(imName).concat('.csv');
    //creating an invisible element
    var element = document.createElement('a');
    element.setAttribute('href', canvIm);
    element.setAttribute('download', canvIm);
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
}
$( "#hideme" ).click(function() {
  $( "#arch" ).toggle( "slow", function() {
  });
});
$( "#hideved" ).click(function() {
  $( "#demoved" ).toggle( "slow", function() {
  });
});
// To display csv table
/*$(document).ready(function(){
 $('#load_data').click(function(){
  $.ajax({
   url:"/data/Test/HorizontalBar/hb1/data_hb1.csv",
   dataType:"text",
   success:function(data)
   {
    var employee_data = data.split(/\r?\n|\r/);
    var table_data = '<table class="table table-bordered table-striped">';
    for(var count = 0; count<employee_data.length; count++)
    {
     var cell_data = employee_data[count].split(",");
     table_data += '<tr>';
     for(var cell_count=0; cell_count<cell_data.length; cell_count++)
     {
      if(count === 0)
      {
       table_data += '<th>'+cell_data[cell_count]+'</th>';
      }
      else
      {
       table_data += '<td>'+cell_data[cell_count]+'</td>';
      }
     }
     table_data += '</tr>';
    }
    table_data += '</table>';
    $('#employee_table').html(table_data);
   }
  });
 });
});*/

