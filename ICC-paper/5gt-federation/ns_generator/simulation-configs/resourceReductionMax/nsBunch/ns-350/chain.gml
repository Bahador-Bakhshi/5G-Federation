graph [
  node [
    id 0
    label 1
    disk 3
    cpu 4
    memory 4
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 1
    memory 12
  ]
  node [
    id 2
    label 3
    disk 6
    cpu 4
    memory 4
  ]
  node [
    id 3
    label 4
    disk 1
    cpu 3
    memory 7
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 3
    memory 9
  ]
  node [
    id 5
    label 6
    disk 2
    cpu 3
    memory 8
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 25
    bw 127
  ]
  edge [
    source 0
    target 1
    delay 35
    bw 194
  ]
  edge [
    source 0
    target 2
    delay 25
    bw 174
  ]
  edge [
    source 1
    target 4
    delay 35
    bw 136
  ]
  edge [
    source 2
    target 3
    delay 29
    bw 150
  ]
  edge [
    source 4
    target 5
    delay 28
    bw 165
  ]
]
