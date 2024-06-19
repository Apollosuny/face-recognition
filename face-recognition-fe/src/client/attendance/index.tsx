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
} from "@mui/material";
import axios from "axios";
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
      <Grid container spacing={5}>
        <Grid item xs={6}>
          <Box
            sx={{
              backgroundColor: "#fff",
              borderRadius: "10px",
              padding: "24px",
            }}
          >
            <Box
              sx={{
                height: "400px",
                border: "1px solid rgba(0, 0, 0, 0.7)",
                borderRadius: "14px",
              }}
            >
              <img ref={videoRef} alt="Video Stream" />
            </Box>
            <Box>
              <Button variant="outlined" onClick={toggleCamera}>
                {cameraOn ? "Turn Off Camera" : "Turn On Camera"}
              </Button>
            </Box>
          </Box>
        </Grid>
        <Grid item xs={6}>
          <TableContainer component={Paper}>
            <Table>
              <TableHead>
                <TableRow>
                  <TableCell>No</TableCell>
                  <TableCell>Fullname</TableCell>
                  <TableCell>Date of Birth</TableCell>
                  <TableCell>Address</TableCell>
                  <TableCell>Actions</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                <TableRow>
                  <TableCell>1</TableCell>
                  <TableCell>Trần Bảo Trung</TableCell>
                  <TableCell>06/09/2003</TableCell>
                  <TableCell>Hanoi</TableCell>
                  <TableCell>Edit</TableCell>
                </TableRow>
              </TableBody>
            </Table>
          </TableContainer>
        </Grid>
      </Grid>
    </Container>
  );
};

export default Attendance;
