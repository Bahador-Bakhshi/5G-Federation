graph [
  node [
    id 0
    label 1
    disk 6
    cpu 3
    memory 5
  ]
  node [
    id 1
    label 2
    disk 8
    cpu 3
    memory 5
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 3
    memory 6
  ]
  node [
    id 3
    label 4
    disk 7
    cpu 1
    memory 13
  ]
  node [
    id 4
    label 5
    disk 3
    cpu 3
    memory 7
  ]
  node [
    id 5
    label 6
    disk 2
    cpu 1
    memory 12
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 32
    bw 186
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 161
  ]
  edge [
    source 1
    target 2
    delay 31
    bw 63
  ]
  edge [
    source 1
    target 3
    delay 33
    bw 132
  ]
  edge [
    source 1
    target 4
    delay 27
    bw 149
  ]
  edge [
    source 3
    target 5
    delay 27
    bw 73
  ]
]
