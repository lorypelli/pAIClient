<script lang="ts">
    let token = '';
</script>

<div class="flex h-max flex-col items-center justify-center space-y-1">
    <span>Token:</span>
    <textarea
        class="resize-none rounded-xl border-2 border-black"
        bind:value={token}
    />
    <button
        class="w-60 rounded-xl border-2 border-black"
        disabled={token.trim() == ''}
        on:click={() => {
            fetch('/api/login', {
                method: 'POST',
                body: JSON.stringify({
                    'token': token
                })
            })
            window.location.href = '/';
        }}>Login</button
    >
</div>
