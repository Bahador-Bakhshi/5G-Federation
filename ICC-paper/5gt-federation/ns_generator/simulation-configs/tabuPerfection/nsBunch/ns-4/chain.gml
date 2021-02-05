graph [
  node [
    id 0
    label 1
    disk 8
    cpu 1
    memory 9
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 1
    memory 10
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 3
    memory 7
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 1
    memory 1
  ]
  node [
    id 4
    label 5
    disk 7
    cpu 4
    memory 1
  ]
  node [
    id 5
    label 6
    disk 6
    cpu 2
    memory 16
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 29
    bw 104
  ]
  edge [
    source 0
    target 1
    delay 28
    bw 191
  ]
  edge [
    source 1
    target 2
    delay 34
    bw 118
  ]
  edge [
    source 1
    target 3
    delay 27
    bw 148
  ]
  edge [
    source 2
    target 4
    delay 34
    bw 170
  ]
  edge [
    source 3
    target 5
    delay 33
    bw 62
  ]
  edge [
    source 4
    target 5
    delay 31
    bw 179
  ]
]
