graph [
  node [
    id 0
    label 1
    disk 1
    cpu 2
    memory 9
  ]
  node [
    id 1
    label 2
    disk 8
    cpu 2
    memory 4
  ]
  node [
    id 2
    label 3
    disk 7
    cpu 4
    memory 7
  ]
  node [
    id 3
    label 4
    disk 3
    cpu 4
    memory 4
  ]
  node [
    id 4
    label 5
    disk 9
    cpu 4
    memory 3
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 2
    memory 4
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 33
    bw 118
  ]
  edge [
    source 0
    target 1
    delay 30
    bw 175
  ]
  edge [
    source 1
    target 2
    delay 30
    bw 132
  ]
  edge [
    source 2
    target 3
    delay 33
    bw 73
  ]
  edge [
    source 3
    target 4
    delay 30
    bw 65
  ]
  edge [
    source 3
    target 5
    delay 27
    bw 192
  ]
]
