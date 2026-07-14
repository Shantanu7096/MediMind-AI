// ==========================================================
// MediMind AI Chatbot
// chatbot.js
// ==========================================================

document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("chatForm");
    const input = document.getElementById("message");
    const sendBtn = document.getElementById("sendBtn");
    const chatBox = document.getElementById("chatMessages");

    if (!form) return;

    //--------------------------------------------------------
    // Auto Scroll
    //--------------------------------------------------------

    function scrollBottom() {

        chatBox.scrollTop = chatBox.scrollHeight;

    }

    scrollBottom();

    //--------------------------------------------------------
    // Loading Bubble
    //--------------------------------------------------------

    function loadingBubble() {

        return `
        <div class="chat-message chat-ai" id="typing">

            <div class="chat-bubble">

                <span class="spinner-border spinner-border-sm"></span>

                Thinking...

            </div>

        </div>
        `;

    }

    //--------------------------------------------------------
    // User Bubble
    //--------------------------------------------------------

    function userBubble(message) {

        return `
        <div class="chat-message chat-user">

            <div class="chat-bubble">

                ${message}

            </div>

        </div>
        `;

    }

    //--------------------------------------------------------
    // AI Bubble
    //--------------------------------------------------------

    function aiBubble(message) {

        return `
        <div class="chat-message chat-ai">

            <div class="chat-bubble">

                ${message.replace(/\n/g,"<br>")}

            </div>

        </div>
        `;

    }

    //--------------------------------------------------------
    // Submit
    //--------------------------------------------------------

    form.addEventListener("submit", async function(e){

        e.preventDefault();

        let message = input.value.trim();

        if(message===""){

            return;

        }

        chatBox.insertAdjacentHTML(

            "beforeend",

            userBubble(message)

        );

        input.value="";

        chatBox.insertAdjacentHTML(

            "beforeend",

            loadingBubble()

        );

        scrollBottom();

        sendBtn.disabled=true;

        sendBtn.innerHTML=`
        <span class="spinner-border spinner-border-sm"></span>
        Sending...
        `;

        try{

            const response=await fetch(

                "/chatbot",

                {

                    method:"POST",

                    headers:{

                        "Content-Type":"application/json"

                    },

                    body:JSON.stringify({

                        message:message

                    })

                }

            );

            const data=await response.json();

            const typing=document.getElementById(

                "typing"

            );

            if(typing){

                typing.remove();

            }

            chatBox.insertAdjacentHTML(

                "beforeend",

                aiBubble(data.reply)

            );

            scrollBottom();

        }

        catch(error){

            const typing=document.getElementById(

                "typing"

            );

            if(typing){

                typing.remove();

            }

            chatBox.insertAdjacentHTML(

                "beforeend",

                aiBubble(

                    "⚠️ Unable to connect to AI server."

                )

            );

        }

        sendBtn.disabled=false;

        sendBtn.innerHTML=`

        <i class="fa-solid fa-paper-plane"></i>

        Send

        `;

        input.focus();

        scrollBottom();

    });

    //--------------------------------------------------------
    // Enter Key
    //--------------------------------------------------------

    input.addEventListener(

        "keydown",

        function(e){

            if(

                e.key==="Enter"

                &&

                !e.shiftKey

            ){

                e.preventDefault();

                form.dispatchEvent(

                    new Event("submit")

                );

            }

        }

    );

});