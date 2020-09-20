graph [
  node [
    id 0
    label 1
    disk 10
    cpu 3
    memory 13
  ]
  node [
    id 1
    label 2
    disk 4
    cpu 2
    memory 2
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 1
    memory 14
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 1
    memory 8
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 1
    memory 1
  ]
  node [
    id 5
    label 6
    disk 9
    cpu 3
    memory 3
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 29
    bw 127
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 160
  ]
  edge [
    source 0
    target 2
    delay 27
    bw 198
  ]
  edge [
    source 0
    target 3
    delay 32
    bw 57
  ]
  edge [
    source 1
    target 5
    delay 29
    bw 195
  ]
  edge [
    source 2
    target 4
    delay 31
    bw 63
  ]
  edge [
    source 3
    target 5
    delay 35
    bw 58
  ]
  edge [
    source 4
    target 5
    delay 27
    bw 127
  ]
]
