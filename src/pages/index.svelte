<script lang="ts">
    import cookie from 'cookiejs';
    let message = '';
    let disabled = false;
    if (!cookie.get('token')) {
        window.location.href = '/login';
    }
    if (!cookie.get('model') || !['gpt-3.5-turbo', 'gpt-4', 'gpt-4-turbo'].includes(cookie.get('model').toString())) {
        cookie.set('model', 'gpt-3.5-turbo');
    }
    if (!cookie.get('prompt')) {
        cookie.set('prompt', '');
    }
</script>

<div class="relative h-container w-container rounded-2xl border-2 border-black">
    <div class="h-12 w-full">
        <button
            class="absolute m-4 mr-2 h-7 w-24 rounded-2xl border-2 border-black bg-white"
            on:click={() => {
                window.location.href = '/settings';
            }}>Settings</button
        >
    </div>
    <textarea
        class="absolute bottom-0 m-4 h-20 w-container_fit resize-none rounded-2xl border-2 border-black"
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
        }}>Submit</button
    >
    <div
        id="container"
        class="flex max-h-container_fit flex-col overflow-auto p-4 pt-2"
    />
</div>
