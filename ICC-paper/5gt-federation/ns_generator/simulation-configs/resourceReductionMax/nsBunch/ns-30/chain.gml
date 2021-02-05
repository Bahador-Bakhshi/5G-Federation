graph [
  node [
    id 0
    label 1
    disk 3
    cpu 1
    memory 2
  ]
  node [
    id 1
    label 2
    disk 9
    cpu 4
    memory 11
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 1
    memory 15
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 1
    memory 4
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 2
    memory 12
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 3
    memory 10
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 111
  ]
  edge [
    source 0
    target 1
    delay 34
    bw 179
  ]
  edge [
    source 1
    target 2
    delay 34
    bw 118
  ]
  edge [
    source 2
    target 3
    delay 30
    bw 91
  ]
  edge [
    source 2
    target 4
    delay 25
    bw 104
  ]
  edge [
    source 3
    target 5
    delay 31
    bw 156
  ]
  edge [
    source 4
    target 5
    delay 28
    bw 142
  ]
]
