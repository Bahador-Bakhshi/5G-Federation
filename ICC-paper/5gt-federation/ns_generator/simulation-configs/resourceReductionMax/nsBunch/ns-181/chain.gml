graph [
  node [
    id 0
    label 1
    disk 6
    cpu 2
    memory 4
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 3
    memory 6
  ]
  node [
    id 2
    label 3
    disk 3
    cpu 1
    memory 7
  ]
  node [
    id 3
    label 4
    disk 2
    cpu 4
    memory 14
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 2
    memory 10
  ]
  node [
    id 5
    label 6
    disk 10
    cpu 3
    memory 2
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 25
    bw 183
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 106
  ]
  edge [
    source 0
    target 2
    delay 34
    bw 162
  ]
  edge [
    source 1
    target 3
    delay 27
    bw 195
  ]
  edge [
    source 2
    target 3
    delay 30
    bw 95
  ]
  edge [
    source 3
    target 4
    delay 34
    bw 192
  ]
  edge [
    source 4
    target 5
    delay 25
    bw 158
  ]
]
