"use client";

import {
  Box,
  Button,
  Container,
  Grid,
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Typography,
} from "@mui/material";
import axios from "axios";
import Image from "next/image";
import { useEffect, useRef, useState } from "react";

interface AttendanceProps {}

const Attendance: React.FC<AttendanceProps> = () => {
  const videoRef = useRef<HTMLImageElement>(null);
  const [cameraOn, setCameraOn] = useState<boolean>(false);

  useEffect(() => {
    const video = videoRef.current;
    if (!video) return;
    if (cameraOn) {
      videoRef.current.src = "http://127.0.0.1:8000/api/ai/detect/";
    } else {
      videoRef.current.src = "";
    }
  }, [cameraOn]);

  const toggleCamera = () => {
    axios
      .post("http://127.0.0.1:8000/api/ai/toggle_camera/")
      .then((response) => {
        setCameraOn(response.data.camera_on);
      })
      .catch((err) => console.error("Error toggling camera:", err));
  };
  return (
    <Container maxWidth="xl">
      <Grid
        container
        spacing={5}
        sx={{
          display: "flex",
          justifyContent: "center",
        }}
      >
        <Grid item xs={8}>
          <Box
            sx={{
              backgroundColor: "#fff",
              borderRadius: "10px",
              padding: "24px",
              boxShadow:
                "rgba(14, 63, 126, 0.06) 0px 0px 0px 1px, rgba(42, 51, 70, 0.03) 0px 1px 1px -0.5px, rgba(42, 51, 70, 0.04) 0px 2px 2px -1px, rgba(42, 51, 70, 0.04) 0px 3px 3px -1.5px, rgba(42, 51, 70, 0.03) 0px 5px 5px -2.5px, rgba(42, 51, 70, 0.03) 0px 10px 10px -5px, rgba(42, 51, 70, 0.03) 0px 24px 24px -8px",
            }}
          >
            <Box textAlign={"center"}>
              <Typography sx={{ fontSize: "40px", fontWeight: 600 }}>
                Face recognition
              </Typography>
            </Box>
            <Box
              sx={{
                height: "400px",
                border: "1px solid rgba(0, 0, 0, 0.7)",
                borderRadius: "14px",
                overflow: "hidden",
                m: "24px 0",
              }}
            >
              {cameraOn ? (
                <img ref={videoRef} alt="Video Stream" />
              ) : (
                <Image
                  src={
                    "https://images.pexels.com/photos/17484899/pexels-photo-17484899/free-photo-of-an-artist-s-illustration-of-artificial-intelligence-ai-this-image-represents-the-boundaries-set-in-place-to-secure-safe-accountable-biotechnology-it-was-created-by-khyati-trehan-as-pa.png?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
                  }
                  quality={100}
                  width={500}
                  height={400}
                  alt="Default Banner"
                  style={{
                    width: "100%",
                    height: "100%",
                    objectFit: "cover",
                  }}
                />
              )}
            </Box>
            <Box
              sx={{
                mt: "24px",
                display: "flex",
                justifyContent: "center",
              }}
            >
              <Button variant="outlined" onClick={toggleCamera}>
                {cameraOn ? "Turn Off Camera" : "Turn On Camera"}
              </Button>
            </Box>
          </Box>
        </Grid>
      </Grid>
    </Container>
  );
};

export default Attendance;
