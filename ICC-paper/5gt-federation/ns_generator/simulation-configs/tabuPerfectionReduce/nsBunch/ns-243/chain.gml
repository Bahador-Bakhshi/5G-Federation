graph [
  node [
    id 0
    label 1
    disk 4
    cpu 2
    memory 3
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 2
    memory 15
  ]
  node [
    id 2
    label 3
    disk 4
    cpu 1
    memory 4
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 1
    memory 1
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 4
    memory 11
  ]
  node [
    id 5
    label 6
    disk 2
    cpu 3
    memory 6
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 33
    bw 120
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 52
  ]
  edge [
    source 1
    target 2
    delay 30
    bw 128
  ]
  edge [
    source 2
    target 3
    delay 29
    bw 63
  ]
  edge [
    source 2
    target 4
    delay 26
    bw 96
  ]
  edge [
    source 2
    target 5
    delay 28
    bw 144
  ]
]
