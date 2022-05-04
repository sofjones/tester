<script>
	import VideoPlayer from './video-player.svelte';
	import Intro from './intro.svelte'
	
	const videoURL = 'https://ia601602.us.archive.org/11/items/Rick_Astley_Never_Gonna_Give_You_Up/Rick_Astley_Never_Gonna_Give_You_Up.mp4'
	let time = 0;
	let play = true;
	let sound = true;
	const name = 'Sofia Jones';
	
	function playVid(){
		let vid = document.getElementById('vid');
		if(play){
			vid.pause();
			play = false;
		}
		else{
			vid.play();
			play = true;
		}
	}
	
	function muteVid(){
	let vid = document.getElementById('vid');
	if(!vid.muted){
		vid.muted = true;
		sound = false;
	}
	else{
		vid.muted = false;
	}
	}

</script>
<div>
	<button on:click={playVid}>
		Play
	</button>
	<button on:click={muteVid}>Mute</button>
	<video
		id='vid'
		src={videoURL}
		type="video/mp4"
		autoplay=true
		bind:currentTime={time}>
		<track kind="captions">
	</video>
</div>

<h1>
	Coding Exercise: Rickroll Me
</h1>

{#if name}
	<h2>
		Submitted by: {name}
	</h2>
{/if}

<Intro />
