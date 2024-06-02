<script lang="ts">
    interface Chat {
        You: string;
        OpenAI: string;
    }
    let message = '';
    let disabled = false;
    let stopped: boolean;
    let controller: AbortController;
    let messages: Chat[] = [];
    async function makeRequest() {
        stopped = false;
        const container = document.querySelector('#container');
        const msg = document.createElement('span');
        msg.innerText = 'You:\n' + message;
        if (container) {
            container.appendChild(msg);
        }
        disabled = true;
        const response = document.createElement('span');
        if (container) {
            container.appendChild(response);
        }
        controller = new AbortController();
        const res = await fetch('/api/response', {
            signal: controller.signal,
            method: 'POST',
            body: JSON.stringify({
                message: message,
            }),
        });
        if (res.body) {
            const reader = res.body.getReader();
            response.innerText = 'OpenAI:\n';
            let data = '';
            while (true) {
                const { done, value } = await reader.read();
                if (done) {
                    break;
                }
                const chunck = new TextDecoder().decode(value);
                response.innerText += chunck;
                data += chunck;
            }
            messages.push({
                You: message,
                OpenAI: data,
            });
        }
        message = '';
        disabled = false;
        stopped = true;
    }
</script>

<div class="h-container w-container relative rounded-2xl border-2 border-black">
    <div class="h-12 w-full">
        <button
            class="absolute m-4 h-7 w-24 rounded-2xl border-2 border-black bg-white"
            on:click={() => {
                window.location.href = '/settings';
            }}>Settings</button
        >
        <button
            class="absolute right-0 m-4 h-7 w-32 rounded-2xl border-2 border-black bg-white"
            on:click={() => {
                const file = new File([JSON.stringify(messages)], 'chat.json');
                const url = window.URL.createObjectURL(file);
                const a = document.createElement('a');
                a.style.display = 'none';
                a.href = url;
                a.download = 'chat.json';
                document.body.appendChild(a);
                a.click();
                window.URL.revokeObjectURL(url);
                document.body.removeChild(a);
            }}>Download</button
        >
    </div>
    <div class="flex justify-center">
        <button
            class="{stopped == false
                ? 'block'
                : 'hidden'} absolute bottom-32 rounded-md border-4 border-gray-500 bg-black text-white"
            on:click={() => {
                controller.abort();
                stopped = true;
                disabled = false;
            }}>Stop Generating</button
        >
    </div>
    <div class="flex justify-center">
        <span class="absolute bottom-24 flex"
            >Shift + Enter to create a newline</span
        >
    </div>
    <textarea
        class="w-container_fit absolute bottom-0 m-4 h-20 resize-none rounded-2xl border-2 border-black"
        bind:value={message}
        on:keydown={async (e) => {
            if (!e.shiftKey && e.key == 'Enter') {
                await makeRequest();
            }
        }}
    />
    <button
        class="absolute bottom-0 right-0 m-4 mr-2 h-20 w-24 rounded-2xl border-2 border-black"
        disabled={message.trim() == '' || disabled}
        on:click={async () => {
            await makeRequest();
        }}>Submit</button
    >
    <div
        id="container"
        class="max-h-container_fit flex flex-col overflow-auto p-4 pt-2"
    />
</div>
