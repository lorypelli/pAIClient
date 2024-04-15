<script lang="ts">
    import cookie from 'cookiejs';
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
            cookie('token', token, { expires: 14, secure: true });
            window.location.href = '/';
        }}>Login</button
    >
</div>
