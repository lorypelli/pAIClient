<script lang="ts">
    interface Chat {
        You: string;
        OpenAI: string;
    }
    let token = '';
    fetch('/api/token').then((res) => {
        res.text().then((data) => {
            token = data;
        });
    });
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
            headers: {
                Authorization: token,
            },
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
                if (container) {
                    container.scrollTop = container.scrollHeight;
                }
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

<div
    class="h-container w-container relative rounded-2xl border-2 border-black dark:border-white"
>
    <div class="h-12">
        <a href="/settings">
            <button
                class="bg-primary text-primary_dark dark:bg-primary_dark dark:text-primary absolute m-4 h-7 w-32 rounded-2xl border-2 border-black dark:border-white"
                >Settings</button
            >
        </a>
        <button
            class="bg-primary text-primary_dark dark:bg-primary_dark dark:text-primary absolute right-0 m-4 h-7 w-32 rounded-2xl border-2 border-black dark:border-white"
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
                : 'hidden'} text-primary absolute bottom-32 rounded-md border-4 border-gray-500 bg-black"
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
        class="w-container_fit bg-primary text-primary_dark dark:bg-primary_dark dark:text-primary absolute bottom-0 m-4 h-20 resize-none rounded-2xl border-2 border-black dark:border-white"
        bind:value={message}
        on:keydown={async (e) => {
            if (e.key == 'Enter' && (message.trim() == '' || disabled)) {
                e.preventDefault();
                return;
            }
            if (!e.shiftKey && e.key == 'Enter') {
                e.preventDefault();
                await makeRequest();
            }
        }}
    />
    <button
        class="text-primary_dark dark:text-primary absolute bottom-0 right-0 m-4 mr-2 h-20 w-24 rounded-2xl border-2 border-black dark:border-white"
        disabled={message.trim() == '' || disabled}
        on:click={async () => {
            if (message.trim() != '' && !disabled) {
                await makeRequest();
            }
        }}>Submit</button
    >
    <div
        id="container"
        class="max-h-container_fit flex flex-col overflow-auto p-4 pt-2"
    />
</div>
