
/* credit: code taken from https://github.com/Code-Institute-Solutions/TaskManagerAuth/tree/main/08-SearchingWithinTheDatabase/01-text_index_searching*/

/*
    jQuery for MaterializeCSS initialization
*/

$(document).ready(function () {
    $(".sidenav").sidenav({edge: "right"});
    $('select').formSelect();
    $('.collapsible').collapsible();
    $("select").formSelect({
            done: "Select"
});

validateMaterializeSelect();
function validateMaterializeSelect() {
    let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
    let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
    if ($("select.validate").prop("required")) {
        $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
    }
    $(".select-wrapper input.select-dropdown").on("focusin", function () {
        $(this).parent(".select-wrapper").on("change", function () {
            if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                $(this).children("input").css(classValid);
            }
        });
    }).on("click", function () {
        if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
            $(this).parent(".select-wrapper").children("input").css(classValid);
        } else {
            $(".select-wrapper input.select-dropdown").on("focusout", function () {
                if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                    if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                        $(this).parent(".select-wrapper").children("input").css(classInvalid);
                    }
                }
            });
        }
    });
}
});


/* 
    INVOICE PAGE 
*/

/* credit: code taken from https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_tolocaledatestring and edited to fit project needs */
             function myFunction() {
                const options = {year: 'numeric', month: 'long', day: 'numeric' };
                var d = new Date();
                var n = d.toLocaleDateString('en-US', options);
                document.getElementById("demo").innerHTML = n;
            }

            /* credit: thank you to Joshua Ugba for helping me make Python and JavaScript communicate with each other */
            let clientInfoList =  []
            fetch('/api/invoice')
                .then(res => res.json())
                .then(list => clientInfoList = list)

            function changeRate() {
                let email = document.getElementById('client_organization').value
                let client = clientInfoList.filter((client) => client.client_email == email)[0]
                document.getElementById('clientName').innerHTML = `<p>${client.client_name}</p>`
                document.getElementById('clientPosition').innerHTML = `<p>${client.client_position}</p>`
                document.getElementById('clientEmail').innerHTML =`<p>${client.client_email}</p>`
            }
            
            /* credit: code taken from https://www.codegrepper.com/code-examples/javascript/calculate+two+number+and+diplay+next+field+without+reload+the+page+javascript and edited to fit project needs */
            var text1 = document.getElementById("interpreting_amount");
            var text2 = document.getElementById("consulting_amount");

            function add_number() {
                var first_number = parseFloat(text1.value);
                if (isNaN(first_number)) first_number = 0;
                var second_number = parseFloat(text2.value);
                if (isNaN(second_number)) second_number = 0;
                var result = first_number + second_number;
                document.getElementById("txtresult").value = result;
            }

/* credit: code taken from https://www.html2pdfrocket.com/Examples/javascript and edited to fit project needs */            
/**
* html: HTML string to convert to PDF
* savePdf: Callback for saving PDF
* Opens the PDF in a new tab, and returns it as a data URI
*/
function pdfRocket(html, savePdf) {
       var self = this;
       
       self.save = savePdf;
       self.req = new XMLHttpRequest();
  
       var url = "https://api.html2pdfrocket.com/pdf";
       var apiKey = "dc67c5f0-34b7-48c2-be1d-ccee3b855f7d";
       var UseGrayscale = true;
 
       var data = "apikey=" + apiKey + "&value=" + encodeURIComponent(html) + UseGrayscale;
  
       self.req.onload = function(event) {
              self.reader = new FileReader();
              
              self.reader.addEventListener("loadend", function() {
 
                     // Open in new tab
                     window.open(self.reader.result, "_blank");
                     
                     // return data URI
                     return self.reader.result;
              });
              
              self.reader.readAsDataURL(self.req.response);
       };
  
       self.req.open("POST", url, true);
       self.req.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
       self.req.responseType = "blob";
  
       self.req.send(data);
}