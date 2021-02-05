graph [
  node [
    id 0
    label 1
    disk 5
    cpu 3
    memory 1
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 1
    memory 4
  ]
  node [
    id 2
    label 3
    disk 8
    cpu 4
    memory 7
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 1
    memory 14
  ]
  node [
    id 4
    label 5
    disk 9
    cpu 3
    memory 7
  ]
  node [
    id 5
    label 6
    disk 2
    cpu 2
    memory 6
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 25
    bw 96
  ]
  edge [
    source 0
    target 1
    delay 30
    bw 168
  ]
  edge [
    source 0
    target 2
    delay 30
    bw 166
  ]
  edge [
    source 0
    target 3
    delay 32
    bw 128
  ]
  edge [
    source 1
    target 4
    delay 27
    bw 71
  ]
  edge [
    source 2
    target 4
    delay 32
    bw 195
  ]
  edge [
    source 4
    target 5
    delay 32
    bw 86
  ]
]
