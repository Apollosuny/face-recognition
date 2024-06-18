"use client";

import {
  Box,
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
import { useEffect, useRef } from "react";

interface AttendanceProps {}

const Attendance: React.FC<AttendanceProps> = () => {
  const videoRef = useRef<HTMLVideoElement>(null);

  useEffect(() => {
    const video = videoRef.current;
    if (!video) return;

    const url = "http://127.0.0.1:8000/api/ai/detect";
    video.src = url;
  }, []);
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
              <video ref={videoRef} autoPlay controls />
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
