<script lang="ts">
    let message = '';
    let disabled = false;
</script>

<div class="h-container w-container relative rounded-2xl border-2 border-black">
    <div class="h-12 w-full">
        <button
            class="absolute m-4 mr-2 h-7 w-24 rounded-2xl border-2 border-black bg-white"
            on:click={() => {
                window.location.href = '/settings';
            }}>Settings</button
        >
    </div>
    <textarea
        class="w-container_fit absolute bottom-0 m-4 h-20 resize-none rounded-2xl border-2 border-black"
        bind:value={message}
    />
    <button
        class="absolute bottom-0 right-0 m-4 mr-2 h-20 w-24 rounded-2xl border-2 border-black"
        disabled={message.trim() == '' || disabled}
        on:click={() => {
            const container = document.querySelector('#container');
            const msg = document.createElement('span');
            msg.innerText = 'You: ' + message;
            if (container) {
                container.appendChild(msg);
            }
            disabled = true;
            const response = document.createElement('span');
            response.innerText = 'OpenAI: Loading...';
            if (container) {
                container.appendChild(response);
            }
            fetch('/api/response', {
                method: 'POST',
                body: JSON.stringify({
                    message: message,
                }),
            }).then((res) => {
                res.text().then((data) => {
                    if (data == 'null') {
                        window.location.reload();
                    }
                    response.innerText = 'OpenAI: ' + data;
                });
            });
            message = '';
            disabled = false;
        }}>Submit</button
    >
    <div
        id="container"
        class="max-h-container_fit flex flex-col overflow-auto p-4 pt-2"
    />
</div>
