<script lang="ts">
    import cookie from 'cookiejs';
    if (!cookie.get("token")) {
        window.location.href = '/login';
    }
    if (!cookie.get('model') || !['gpt-3.5-turbo', 'gpt-4', 'gpt-4-turbo'].includes(cookie.get('model').toString())) {
        cookie.set('model', 'gpt-3.5-turbo');
    }
    if (!cookie.get('prompt')) {
        cookie.set('prompt', '');
    }
    let model = cookie.get('model').toString();
    let prompt = cookie.get('prompt').toString();
</script>

<div class="flex h-max flex-col items-center justify-center space-y-1">
    <span>Model:</span>
    <select bind:value={model}>
        <option class="text-center">gpt-4-turbo</option>
        <option class="text-center">gpt-4</option>
        <option class="text-center">gpt-3.5-turbo</option>
    </select>
    <span>Prompt:</span>
    <textarea
        class="resize-none rounded-xl border-2 border-black"
        bind:value={prompt}
        rows="10"
    />
    <button
        class="w-60 rounded-xl border-2 border-black"
        disabled={prompt.trim() == ''}
        on:click={() => {
            cookie('model', model, { expires: 30, secure: true });
            cookie('prompt', prompt, { expires: 30, secure: true });
            window.location.href = '/';
        }}>Save</button
    >
</div>
