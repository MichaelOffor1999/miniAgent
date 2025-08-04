user_input = document.getElementById("user-input");
button = document.getElementById("sendButton");
output = document.getElementById("response-box");

button.disabled = true;



user_input.addEventListener("input", () => {
    const value = user_input.value.trim();
    button.disabled = value === "";
    
});

button.addEventListener("click", async () => {
    const value = user_input.value.trim();
    if(!value){
        output.textContent = "Please valid input"
    }

    const response = await fetch("/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({"message": value})
    })

    data = await response.json();

    if(data.reply){
        output.textContent = data.reply;
    }else{
        output.textContent = data.error || "Somthing went wrong";
    }
});