graph [
  node [
    id 0
    label 1
    disk 3
    cpu 1
    memory 7
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 4
    memory 5
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 2
    memory 6
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 4
    memory 7
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 2
    memory 15
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 1
    memory 5
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 116
  ]
  edge [
    source 0
    target 1
    delay 34
    bw 181
  ]
  edge [
    source 0
    target 2
    delay 32
    bw 63
  ]
  edge [
    source 0
    target 3
    delay 33
    bw 185
  ]
  edge [
    source 1
    target 4
    delay 33
    bw 84
  ]
  edge [
    source 4
    target 5
    delay 35
    bw 106
  ]
]
