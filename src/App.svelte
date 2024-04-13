<script lang="ts">
    let message = '';
</script>

<div
    id="container"
    class="relative h-container w-container rounded-2xl border-2 border-black"
>
    <textarea
        class="absolute bottom-0 m-4 h-20 w-container_fit resize-none rounded-2xl border-2 border-black"
        bind:value={message}
    ></textarea>
    <button
        type="submit"
        class="absolute bottom-0 right-0 m-4 mr-2 h-20 w-24 rounded-2xl border-2 border-black"
        disabled={message.trim() == ''}
        on:click={() => {
            const container = document.querySelector('#container');
            const msg = document.createElement('span');
            msg.innerText = message;
            if (container) {
                container.appendChild(msg);
            }
        }}>Submit</button
    >
</div>
