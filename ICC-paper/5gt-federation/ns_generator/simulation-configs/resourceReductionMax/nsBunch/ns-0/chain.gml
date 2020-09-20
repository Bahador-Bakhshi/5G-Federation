graph [
  node [
    id 0
    label 1
    disk 2
    cpu 2
    memory 15
  ]
  node [
    id 1
    label 2
    disk 9
    cpu 4
    memory 6
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 2
    memory 13
  ]
  node [
    id 3
    label 4
    disk 1
    cpu 1
    memory 4
  ]
  node [
    id 4
    label 5
    disk 10
    cpu 4
    memory 12
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 2
    memory 2
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 28
    bw 84
  ]
  edge [
    source 0
    target 1
    delay 35
    bw 89
  ]
  edge [
    source 0
    target 2
    delay 29
    bw 181
  ]
  edge [
    source 0
    target 3
    delay 35
    bw 177
  ]
  edge [
    source 1
    target 4
    delay 28
    bw 121
  ]
  edge [
    source 2
    target 4
    delay 32
    bw 142
  ]
  edge [
    source 3
    target 5
    delay 27
    bw 106
  ]
  edge [
    source 4
    target 5
    delay 31
    bw 74
  ]
]
