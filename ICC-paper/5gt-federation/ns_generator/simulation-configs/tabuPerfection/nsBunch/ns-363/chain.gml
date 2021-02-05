graph [
  node [
    id 0
    label 1
    disk 5
    cpu 3
    memory 3
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 2
    memory 6
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 1
    memory 9
  ]
  node [
    id 3
    label 4
    disk 7
    cpu 2
    memory 13
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 4
    memory 16
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 2
    memory 15
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 35
    bw 185
  ]
  edge [
    source 0
    target 1
    delay 25
    bw 198
  ]
  edge [
    source 0
    target 2
    delay 34
    bw 92
  ]
  edge [
    source 0
    target 3
    delay 32
    bw 70
  ]
  edge [
    source 1
    target 4
    delay 31
    bw 153
  ]
  edge [
    source 2
    target 4
    delay 25
    bw 79
  ]
  edge [
    source 3
    target 4
    delay 29
    bw 63
  ]
  edge [
    source 4
    target 5
    delay 28
    bw 162
  ]
]
