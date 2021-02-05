graph [
  node [
    id 0
    label 1
    disk 8
    cpu 1
    memory 15
  ]
  node [
    id 1
    label 2
    disk 4
    cpu 3
    memory 3
  ]
  node [
    id 2
    label 3
    disk 3
    cpu 4
    memory 4
  ]
  node [
    id 3
    label 4
    disk 5
    cpu 3
    memory 9
  ]
  node [
    id 4
    label 5
    disk 3
    cpu 2
    memory 7
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 1
    memory 6
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 35
    bw 84
  ]
  edge [
    source 0
    target 1
    delay 27
    bw 88
  ]
  edge [
    source 0
    target 2
    delay 29
    bw 175
  ]
  edge [
    source 1
    target 3
    delay 33
    bw 56
  ]
  edge [
    source 2
    target 3
    delay 29
    bw 91
  ]
  edge [
    source 3
    target 4
    delay 26
    bw 83
  ]
  edge [
    source 4
    target 5
    delay 29
    bw 192
  ]
]
