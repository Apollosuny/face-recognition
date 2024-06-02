'use client'
import Image from "next/image";
import { useEffect } from "react";

export default function Home() {
  useEffect(() => {
    const video = document.getElementById('video') as HTMLImageElement;
    if (!video) return
    video.src = "http://localhost:5000/video_feed";
  }, []);

  return (
    <div>
      <h1>Video Feed</h1>
      <img id="video" alt="Video stream" />
    </div>
  );
}
