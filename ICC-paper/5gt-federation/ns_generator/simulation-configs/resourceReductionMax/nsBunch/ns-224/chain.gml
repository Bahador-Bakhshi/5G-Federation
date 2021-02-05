graph [
  node [
    id 0
    label 1
    disk 5
    cpu 4
    memory 3
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 2
    memory 3
  ]
  node [
    id 2
    label 3
    disk 8
    cpu 3
    memory 7
  ]
  node [
    id 3
    label 4
    disk 1
    cpu 2
    memory 8
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 2
    memory 3
  ]
  node [
    id 5
    label 6
    disk 6
    cpu 2
    memory 5
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 200
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 158
  ]
  edge [
    source 0
    target 2
    delay 30
    bw 198
  ]
  edge [
    source 0
    target 3
    delay 29
    bw 178
  ]
  edge [
    source 2
    target 4
    delay 30
    bw 78
  ]
  edge [
    source 3
    target 5
    delay 33
    bw 186
  ]
]
